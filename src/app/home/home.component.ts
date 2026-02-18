import { Component } from '@angular/core';
import { RouterLink } from '@angular/router';
import { portfolioData } from '../portfolio.data';

@Component({
  selector: 'app-home',
  standalone: true,
  imports: [RouterLink],
  templateUrl: './home.component.html',
  styleUrl: './home.component.css',
})
export class HomeComponent {
  protected data = portfolioData;
  protected currentYear = new Date().getFullYear();
  protected readonly skillCategories = [
    {
      title: 'Frontend',
      skills: ['HTML', 'CSS', 'JavaScript', 'TypeScript', 'Bootstrap', 'Angular', 'React'],
    },
    {
      title: 'Backend & APIs',
      skills: ['C#', '.NET', '.NET Web API', 'ASP.NET Core', 'ASP.NET MVC', 'REST API', 'Entity Framework', 'WPF'],
    },
    {
      title: 'Database & Workflow',
      skills: ['SQL Server', 'Stored Procedures', 'Authentication', 'Authorization', 'Git', 'Agile', 'SDLC'],
    },
  ] as const;
}
