/**
 * Portfolio content sourced from resume (Abinesh_2002.pdf)
 */

/** Link to view live project (website/demo) */
export interface ViewLink {
  label: string;
  url: string;
}

/** Link to source code (e.g. GitHub) */
export interface GitLink {
  label: string;
  url: string;
}

export interface ExperienceProject {
  name: string;
  description: string;
  /** Point-wise details for detail page (15+ points) */
  points?: readonly string[];
  /** Slug for detail page route (e.g. oonsoft, furusaan, business-admin) */
  detailSlug?: string;
  viewLinks?: readonly ViewLink[];
  gitLinks?: readonly GitLink[];
  /** @deprecated use viewLinks/gitLinks */
  links?: readonly { label: string; url: string }[];
}

/** ATS-friendly: machine-readable dates (YYYY-MM) for parsing by HR/ATS systems */
export interface ATSDates {
  start: string;  // e.g. "2024-08"
  end: string;    // e.g. "2024-08" or "present"
  display: string; // e.g. "August 2024 – Present"
}

export interface ExperienceItem {
  company: string;
  role: string;
  type: string;
  period: string;
  atsDates?: ATSDates;
  project?: string;
  description?: string;
  /** Live / view project links (website, demo) */
  viewLinks?: readonly ViewLink[];
  /** Source code links (e.g. GitHub) */
  gitLinks?: readonly GitLink[];
  /** @deprecated use viewLinks */
  links?: readonly { label: string; url: string }[];
  projects?: readonly ExperienceProject[];
}

export const portfolioData = {
  name: 'ABINESH R S',
  tagline: '.NET Developer',
  summary: `.NET Developer with a strong background in designing, developing, and maintaining web and desktop applications. Proficient in C#, ASP.NET Core/MVC, WPF, and API development. Skilled in database management using SQL Server and Entity Framework. Experienced in front-end technologies such as Angular, React, HTML, CSS, and Bootstrap. Passionate about writing clean, maintainable code and collaborating with teams.`,
  contact: {
    phone: '8300893013',
    email: 'abiabinesh483@gmail.com',
  },
  skills: [
    'HTML',
    'CSS',
    'JavaScript',
    'Bootstrap',
    '.NET',
    'WPF',
    'SQL Server',
    'Git',
    'Angular',
    'React',
    'ASP.NET Core',
    'Entity Framework',
  ],
  languages: ['English'],
  /** ATS-friendly: education with clear date ranges */
  education: [
    {
      degree: "Master's Degree in Computer Science",
      period: '2022 – 2024',
      atsDates: { start: '2022', end: '2024', display: '2022 – 2024' },
      grade: 'CGPA 8.14',
      institution: 'Nesamony Memorial Christian College, Marthandam',
    },
    {
      degree: 'Bachelor Degree in Computer Science',
      period: '2019 – 2022',
      atsDates: { start: '2019', end: '2022', display: '2019 – 2022' },
      grade: 'CGPA 7.74',
      institution: 'Nesamony Memorial Christian College, Marthandam',
    },
    {
      degree: '12th Grade',
      period: '2018 – 2019',
      atsDates: { start: '2018', end: '2019', display: '2018 – 2019' },
      grade: '57%',
      institution: 'Hindu Vidyalaya Marthandam, HSS',
    },
    {
      degree: '10th Grade',
      period: '2016 – 2017',
      atsDates: { start: '2016', end: '2017', display: '2016 – 2017' },
      grade: '78%',
      institution: 'Hindu Vidyalaya Marthandam, HSS',
    },
  ],
  experience: [
    {
      company: 'Keesa Express',
      role: '.NET Developer',
      type: 'Full-time',
      period: 'August 2024 – Present',
      atsDates: { start: '2024-08', end: 'present', display: 'August 2024 – Present' },
      projects: [
        {
          name: 'OON SOFT – Digital ESET Keys Purchasing',
          detailSlug: 'oonsoft',
          description: 'Digital ESET antivirus key purchasing system under the OON SOFT brand (oonsoft.llc).',
          points: [
            'Develop and maintain the digital ESET key purchasing system for web and mobile under OON SOFT.',
            'Back end: .NET Web API (C#) for REST APIs, business logic, and key management.',
            'Database: Microsoft SQL Server for orders, keys, and user data.',
            'Stored procedures for order processing, key generation, and reporting.',
            'Front end: React with TypeScript for responsive web and mobile-ready UI.',
            'Languages & markup: HTML5, CSS3, JavaScript/TypeScript, JSX.',
            'State management and API integration with React patterns.',
            'Git for version control; feature branches and code reviews.',
            'Agile methodology: sprints, stand-ups, and timely releases.',
            'Authentication and authorization for secure key purchase flow.',
            'Payment and order tracking integrated in the system.',
            'Admin panel for key inventory and order management.',
            'Responsive design for desktop and mobile browsers.',
            'Error handling, validation, and logging on backend and front end.',
            'Deployment and environment configuration (dev/staging/production).',
            'Cross-functional collaboration with design and QA teams.',
          ],
          viewLinks: [{ label: 'View OON SOFT', url: 'https://oonsoft.llc/' }],
        },
        {
          name: 'Furusaan – Custom Clearance Invoice',
          detailSlug: 'furusaan',
          description: 'Custom Clearance Invoice platform (furusaan.com) for sending and verifying invoices.',
          points: [
            'Build and maintain the Furusaan Custom Clearance Invoice platform for companies.',
            'Back end: .NET Web API (C#) for invoice APIs, validation, and workflows.',
            'Database: SQL Server for invoices, companies, users, and audit data.',
            'Stored procedures for invoice creation, verification, and reporting.',
            'Front end: React/Angular with TypeScript for dashboard and invoice UI.',
            'Languages: HTML, CSS, JavaScript/TypeScript; responsive layouts.',
            'Role-based access: different views for admin, company, and verifiers.',
            'Invoice upload, send, verify, and status tracking end to end.',
            'Git for version control; branching and merge workflows.',
            'Agile practices: sprint planning, demos, and release cycles.',
            'RESTful API design and documentation.',
            'Form validation and error handling on front end and API.',
            'Secure authentication and session management.',
            'Data export and reporting for clearance and compliance.',
            'Integration with existing business and Furusaan ecosystem.',
            'Performance tuning for large invoice datasets and queries.',
            'Collaboration with cross-functional teams for delivery.',
          ],
          viewLinks: [{ label: 'View Furusaan', url: 'https://furusaan.com/' }],
        },
        {
          name: 'Business Admin',
          detailSlug: 'business-admin',
          description: 'Admin and management panel (business.furusaan.com) for the Furusaan ecosystem.',
          points: [
            'Develop and maintain the Business Admin panel for Furusaan business operations.',
            'Back end: .NET Web API (C#) for admin APIs and business logic.',
            'Database: SQL Server for users, roles, settings, and operational data.',
            'Stored procedures for admin reports, user management, and data updates.',
            'Front end: React with TypeScript for admin dashboard and CRUD screens.',
            'Languages: HTML, CSS, JavaScript/TypeScript for UI and forms.',
            'User and role management: create, edit, deactivate users and permissions.',
            'Git for version control; code reviews and release tagging.',
            'Agile methodology: iterations and prioritization with stakeholders.',
            'Secure admin-only access with authentication and authorization.',
            'Audit logging for sensitive admin actions.',
            'Integration with Furusaan and related services for data sync.',
            'Responsive admin UI for desktop and tablet.',
            'Validation and error handling on API and front end.',
            'Deployment and configuration for admin environment.',
            'Documentation and handover for support and operations.',
            'Collaboration with backend and product teams for new features.',
          ],
          viewLinks: [{ label: 'View Business Admin', url: 'https://business.furusaan.com/' }],
        },
      ],
    },
    {
      company: 'Srishti Innovative',
      role: '.NET Developer',
      type: 'Internship',
      period: 'December 2023 – June 2024',
      atsDates: { start: '2023-12', end: '2024-06', display: 'December 2023 – June 2024' },
      projects: [
        {
          name: 'WPF – Hospital Management Project',
          description:
            'Developed a desktop Hospital Management System using .NET and WPF. Features include patient registration, appointments, and records with a user-friendly interface. Data layer with SQL Server and stored procedures. Git and cross-functional collaboration.',
        },
        {
          name: 'School Management Project (SchoolMan)',
          description:
            'Worked on SchoolMan (schoolman.in), an online school management system for school administration, teachers, and parents. Features: online fee collection, parent communication (SMS, email, mobile notifications), school bus GPS tracking, progress reports and marks, attendance management and reports, staff management with biometric system, staff allocation to classes and periods, financial and administrative reports. Web and mobile application (Google Play). Built with .NET and SQL Server. Git for version control.',
          viewLinks: [{ label: 'View SchoolMan', url: 'https://www.schoolman.in/' }],
        },
        {
          name: 'Real Estate Project (Final internship) – Praedium',
          description:
            'Worked on a Real Estate management project (Praedium) in the final phase of the internship. Web-based solution for property listing and management. Front end: React (Create React App). Backend and data with .NET and SQL Server. Git and agile practices. Source code in the repository below.',
          gitLinks: [{ label: 'Praedium (Real Estate)', url: 'https://github.com/AbineshRS/Praedium' }],
        },
      ],
    },
  ],
  github: 'https://github.com/AbineshRS',
} as {
  name: string;
  tagline: string;
  summary: string;
  contact: { phone: string; email: string };
  skills: readonly string[];
  languages: readonly string[];
  education: readonly {
    degree: string;
    period: string;
    atsDates?: { start: string; end: string; display: string };
    grade: string;
    institution: string;
  }[];
  experience: readonly ExperienceItem[];
  github: string;
};

/** Get project by detail slug (for /project/:slug pages) */
export function getProjectBySlug(slug: string): (ExperienceProject & { liveUrl?: string }) | null {
  const keesa = portfolioData.experience.find((e) => e.company === 'Keesa Express');
  if (!keesa?.projects) return null;
  const project = keesa.projects.find((p) => p.detailSlug === slug);
  if (!project) return null;
  const liveUrl = project.viewLinks?.[0]?.url;
  return { ...project, liveUrl };
}
