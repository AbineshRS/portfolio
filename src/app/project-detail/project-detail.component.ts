import { Component } from '@angular/core';
import { ActivatedRoute, RouterLink } from '@angular/router';
import { getProjectBySlug } from '../portfolio.data';

@Component({
  selector: 'app-project-detail',
  standalone: true,
  imports: [RouterLink],
  templateUrl: './project-detail.component.html',
  styleUrl: './project-detail.component.css',
})
export class ProjectDetailComponent {
  project: ReturnType<typeof getProjectBySlug> = null;

  constructor(private route: ActivatedRoute) {
    const slug = this.route.snapshot.paramMap.get('slug') ?? '';
    this.project = getProjectBySlug(slug);
    this.route.paramMap.subscribe((params) => {
      this.project = getProjectBySlug(params.get('slug') ?? '');
    });
  }
}
