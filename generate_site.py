"""
generate_site.py
------------------

This script builds a simple personal website for Sarthak Singh based on
information pulled from his GitHub profile and resume. The output is a
static HTML file (`index.html`) along with a CSS file for styling. To
generate the site, simply run this script from within the project
directory. The generated site includes sections for an introduction,
experience, education, projects, skills, and research. A file upload
control lets you replace the placeholder profile photo at runtime.

Usage:
    python generate_site.py

The script writes to ``index.html`` and assumes there is an ``assets``
directory containing a ``placeholder.png`` image. Feel free to replace
the placeholder with your own photo after generating the site.
"""

import os
from pathlib import Path

# Data structures representing the resume and GitHub profile information.
experiences = [
    {
        "company": "IBM",
        "position": "Software Development Engineer II",
        "duration": "July 2021 – Jan 2024",
        "location": "Kochi, India",
        "technologies": [
            "Python", "AWS", "Kubernetes", "Docker", "Jenkins",
            "PostgreSQL", "Golang"
        ],
        "highlights": [
            "Led the migration of data analytics pipelines from ElasticSearch to OpenSearch, reducing operational costs by up to $3M annually and improving search performance.",
            "Streamlined backend services for API management on IBM Cloud and AWS, optimizing traffic routing, security, and data processing.",
            "Spearheaded a security optimization project for managing sensitive data, earning an IBM Quarterly Cash Award."
        ],
    },
    {
        "company": "Influenced",
        "position": "Full Stack Developer",
        "duration": "July 2024 – June 2025",
        "location": "Remote, USA",
        "technologies": [
            "Next.js", "React", "TypeScript", "Tailwind CSS", "AWS Amplify", "Dynamo DB"
        ],
        "highlights": [
            "Developed an AI‑powered marketplace connecting brands with micro‑influencers, enabling authentic social proof and massive reach.",
            "Implemented role‑based access and AI‑driven workflows for product listings, interest expressions, and collaboration management."
        ],
    },
    {
        "company": "Informatica",
        "position": "Software Engineer Intern",
        "duration": "Jan 2021 – July 2021",
        "location": "Bangalore, India",
        "technologies": [
            "Python", "ETL", "Oracle DB", "Tableau", "Golang", "AWS S3"
        ],
        "highlights": [
            "Resolved over 100 customer support tickets for the Informatica ETL tool, providing technical guidance and troubleshooting.",
            "Integrated the ETL tool with databases such as PostgreSQL, MySQL and AWS S3.",
            "Led an intern showcase demonstrating how the ETL tool integrates with Tableau to transform and visualise a COVID dataset."
        ],
    },
]

education = [
    {
        "institution": "University of Maryland, College Park",
        "degree": "Master of Engineering in Software Engineering",
        "duration": "Jan 2024 – Dec 2025",
        "location": "College Park, MD, USA",
        "gpa": "3.52/4.0",
        "details": [
            "Teaching Assistant for System Design and Scaling, transformer models, FastAPI and Faiss."
        ],
    },
    {
        "institution": "Vellore Institute of Technology",
        "degree": "Bachelor of Technology in Computer Science and Engineering",
        "duration": "June 2017 – May 2021",
        "location": "Vellore, India",
        "gpa": None,
        "details": [],
    },
]

projects = [
    {
        "name": "RAG Expert Assistant",
        "description": (
            "A full Retrieval‑Augmented Generation (RAG) system that lets users "
            "upload documents, generate embeddings, store them in a vector database, "
            "and chat with the content using an LLM‑powered assistant. Built with "
            "Python, LangChain, ChromaDB and Gradio, it demonstrates document "
            "ingestion, intelligent text chunking, vector storage and real‑time context retrieval."
        ),
        "technologies": ["Python", "LangChain", "ChromaDB", "Gradio"],
        "link": "https://github.com/Sarthak-kiloray/Rag-expert-assistant",
    },
    {
        "name": "Transformers Lab",
        "description": (
            "A programming lab exploring the fundamentals of transformer models using "
            "pre‑trained models from the Hugging Face Transformers library. The project "
            "experiments with token prediction, semantic similarity and visualisation of "
            "model outputs to understand how LLMs generate text."
        ),
        "technologies": ["Python", "Hugging Face Transformers"],
        "link": "https://github.com/Sarthak-kiloray/Transformers_lab",
    },
    {
        "name": "DigiSchool",
        "description": (
            "A comprehensive Learning Management System for schools that streamlines "
            "educational processes and enhances collaboration among students, teachers, "
            "administrators and parents. It provides modules for account management, "
            "curriculum management, assessments, performance tracking, collaboration and certificate generation."
        ),
        "technologies": ["React.js", "Spring Boot", "MySQL"],
        "link": "https://github.com/Sarthak-kiloray/DigiSchool",
    },
]

skills = {
    "Programming": [
        "Python", "JavaScript", "Flask", "REST APIs", "SQL (PostgreSQL, MySQL)",
        "NoSQL", "Redis", "Kafka", "Django"
    ],
    "DevOps & Cloud": [
        "AWS", "Docker", "Kubernetes (K8s)", "ArgoCD", "Jenkins", "CI/CD pipelines", "Terraform"
    ],
    "Systems": [
        "Microservices", "Distributed Systems", "Scaling Systems", "Object‑Oriented Design", "Unit Testing"
    ],
    "Other": [
        "Git/GitHub", "Windows", "Linux", "Data Structures & Algorithms", "Communication", "Innovation"
    ],
    "AI & ML": [
        "Cursor", "NLP (transformer models)", "LLM (Claude, GPT)",
        "Deep Learning & ML (PyTorch, SGD, scikit‑learn)", "Gradio"
    ],
}

# Introductory text pulled from the GitHub profile
intro_paragraph = (
    "Hello, my name is Sarthak Singh, and I am a master's in Software Engineering "
    "student at the University of Maryland College Park, graduating in December 2025. "
    "I am a full‑stack software developer with around four years of experience working "
    "as a Software Engineer at IBM India Labs and remotely for Influenced (startup). "
    "I bring expertise in Python, Golang, Kubernetes, CI/CD, AWS, SQL/NoSQL databases, "
    "Docker and web development (Django, FastAPI, etc). My top skills include system "
    "design and data structures. Besides programming, I enjoy sports and outdoor activities."
)

subtitle = (
    "Skilled in building scalable and distributed systems. I build LLM‑based RAG "
    "pipelines and tools for automation."
)

linkedin_url = "https://www.linkedin.com/in/sarthak-singh3867"
github_url = "https://github.com/Sarthak-kiloray"
research_url = "https://www.sciencedirect.com"  # Replace with the specific article link if available


def build_experience_html() -> str:
    """Builds the HTML markup for the experience section."""
    sections = []
    for exp in experiences:
        tech_list = ", ".join(exp["technologies"])
        highlights_list = "".join(f"<li>{h}</li>" for h in exp["highlights"])
        sections.append(
            f"""
            <div class="experience">
                <h3>{exp['position']} – {exp['company']}</h3>
                <span class="duration-location">{exp['duration']} | {exp['location']}</span>
                <p class="technologies"><strong>Technologies:</strong> {tech_list}</p>
                <ul class="highlights">
                    {highlights_list}
                </ul>
            </div>
            """
        )
    return "\n".join(sections)


def build_education_html() -> str:
    """Builds the HTML markup for the education section."""
    sections = []
    for edu in education:
        details_list = "".join(f"<li>{d}</li>" for d in edu["details"])
        gpa_html = f" | GPA: {edu['gpa']}" if edu.get("gpa") else ""
        sections.append(
            f"""
            <div class="education">
                <h3>{edu['degree']}</h3>
                <span class="institution">{edu['institution']}</span>
                <span class="duration-location">{edu['duration']} | {edu['location']}{gpa_html}</span>
                {f'<ul class="details">{details_list}</ul>' if details_list else ''}
            </div>
            """
        )
    return "\n".join(sections)


def build_projects_html() -> str:
    """Builds the HTML markup for the projects section."""
    sections = []
    for proj in projects:
        tech_list = ", ".join(proj["technologies"])
        sections.append(
            f"""
            <div class="project">
                <h3><a href="{proj['link']}" target="_blank" rel="noopener noreferrer">{proj['name']}</a></h3>
                <p class="description">{proj['description']}</p>
                <p class="technologies"><strong>Technologies:</strong> {tech_list}</p>
            </div>
            """
        )
    return "\n".join(sections)


def build_skills_html() -> str:
    """Builds the HTML markup for the skills section."""
    sections = []
    for category, items in skills.items():
        items_list = ", ".join(items)
        sections.append(
            f"""
            <div class="skill-category">
                <h4>{category}</h4>
                <p>{items_list}</p>
            </div>
            """
        )
    return "\n".join(sections)


def generate_html() -> str:
    """Composes the full HTML page as a string."""
    experience_html = build_experience_html()
    education_html = build_education_html()
    projects_html = build_projects_html()
    skills_html = build_skills_html()

    return f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sarthak Singh – Personal Website</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <header>
        <div class="container intro">
            <img id="profile-img" src="assets/placeholder.png" alt="Profile Photo">
            <input type="file" id="photo-upload" accept="image/*">
            <h1>Sarthak Singh</h1>
            <p class="subtitle">{subtitle}</p>
            <div class="links">
                <a href="{linkedin_url}" target="_blank" rel="noopener noreferrer">LinkedIn</a>
                <a href="{github_url}" target="_blank" rel="noopener noreferrer">GitHub</a>
                <a href="{research_url}" target="_blank" rel="noopener noreferrer">Research Article</a>
            </div>
        </div>
    </header>
    <main>
        <section id="about">
            <div class="container">
                <h2>About Me</h2>
                <p>{intro_paragraph}</p>
            </div>
        </section>
        <section id="experience">
            <div class="container">
                <h2>Work Experience</h2>
                {experience_html}
            </div>
        </section>
        <section id="education">
            <div class="container">
                <h2>Education</h2>
                {education_html}
            </div>
        </section>
        <section id="projects">
            <div class="container">
                <h2>Projects</h2>
                {projects_html}
            </div>
        </section>
        <section id="skills">
            <div class="container">
                <h2>Skills</h2>
                <div class="skills-grid">
                    {skills_html}
                </div>
            </div>
        </section>
    </main>
    <footer>
        <div class="container">
            <p>© 2025 Sarthak Singh. All rights reserved.</p>
        </div>
    </footer>
    <script>
    // Preview the uploaded profile photo by setting it as the src of the img tag
    const photoInput = document.getElementById('photo-upload');
    photoInput.addEventListener('change', function(event) {{
        const file = event.target.files[0];
        if (file) {{
            const reader = new FileReader();
            reader.onload = function(e) {{
                document.getElementById('profile-img').src = e.target.result;
            }};
            reader.readAsDataURL(file);
        }}
    }});
    </script>
</body>
</html>
"""


def write_files():
    """Writes the HTML and CSS files to disk."""
    # Ensure we're in the project directory
    project_dir = Path(__file__).resolve().parent
    html_output = project_dir / "index.html"
    css_output = project_dir / "style.css"

    # Generate and write HTML
    html_content = generate_html()
    html_output.write_text(html_content, encoding="utf-8")

    # CSS styling
    css_content = """
/* Basic reset */
* {{
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}}

body {{
    font-family: Arial, sans-serif;
    line-height: 1.6;
    color: #333;
    background-color: #f9f9f9;
}}

.container {{
    width: 90%;
    max-width: 1000px;
    margin: 0 auto;
    padding: 20px;
}}

header {{
    background-color: #0c4a6e;
    color: #fff;
    padding: 40px 0;
    text-align: center;
}}

.intro {{
    display: flex;
    flex-direction: column;
    align-items: center;
}}

header img {{
    width: 150px;
    height: 150px;
    border-radius: 50%;
    object-fit: cover;
    margin-bottom: 15px;
    border: 4px solid #fff;
}}

#photo-upload {{
    margin-bottom: 10px;
}}

.subtitle {{
    font-style: italic;
    margin-top: 10px;
}}

.links a {{
    color: #ffc107;
    text-decoration: none;
    margin: 0 10px;
    font-weight: bold;
}}

.links a:hover {{
    text-decoration: underline;
}}

section {{
    margin-top: 40px;
}}

h2 {{
    margin-bottom: 20px;
    color: #0c4a6e;
    font-size: 1.8rem;
    border-bottom: 2px solid #0c4a6e;
    display: inline-block;
}}

.experience, .education, .project {{
    margin-bottom: 30px;
}}

.duration-location {{
    display: block;
    font-size: 0.9rem;
    color: #555;
    margin-bottom: 5px;
}}

.technologies {{
    font-size: 0.9rem;
    color: #444;
    margin-bottom: 10px;
}}

.highlights, .details {{
    list-style: disc;
    padding-left: 20px;
    margin-bottom: 10px;
}}

.skills-grid {{
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
    gap: 20px;
}}

.skill-category h4 {{
    margin-bottom: 5px;
    color: #0c4a6e;
}}

footer {{
    background-color: #0c4a6e;
    color: #fff;
    text-align: center;
    padding: 20px 0;
    margin-top: 40px;
}}

@media (max-width: 600px) {{
    header img {{
        width: 120px;
        height: 120px;
    }}
}}
"""
    css_output.write_text(css_content, encoding="utf-8")


if __name__ == "__main__":
    write_files()