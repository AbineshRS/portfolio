import { Component } from '@angular/core';
import { Router, RouterLink, RouterOutlet } from '@angular/router';
import { portfolioData } from './portfolio.data';

@Component({
  selector: 'app-root',
  imports: [RouterLink, RouterOutlet],
  templateUrl: './app.html',
  styleUrl: './app.css',
})
export class App {
  protected data = portfolioData;

  constructor(private router: Router) {}

  protected onNavClick(event: Event, fragment: string): void {
    const path = this.router.url.split('?')[0].split('#')[0];
    if (path === '/' || path === '') {
      event.preventDefault();
      const el = document.getElementById(fragment);
      if (el) {
        el.scrollIntoView({ behavior: 'smooth', block: 'start' });
      }
      history.replaceState(null, '', `/#${fragment}`);
    }
  }
}
