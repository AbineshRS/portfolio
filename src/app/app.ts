import { Component, OnInit } from '@angular/core';
import { Router, RouterLink, RouterOutlet } from '@angular/router';
import { portfolioData } from './portfolio.data';

@Component({
  selector: 'app-root',
  imports: [RouterLink, RouterOutlet],
  templateUrl: './app.html',
  styleUrl: './app.css',
})
export class App implements OnInit {
  protected data = portfolioData;
  protected isDarkTheme = false;
  protected mobileMenuOpen = false;
  private readonly themeStorageKey = 'portfolio-theme';

  constructor(private router: Router) {}

  protected toggleMobileMenu(): void {
    this.mobileMenuOpen = !this.mobileMenuOpen;
  }

  protected closeMobileMenu(): void {
    this.mobileMenuOpen = false;
  }

  ngOnInit(): void {
    this.initializeTheme();
  }

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

  protected toggleTheme(): void {
    const nextTheme = this.isDarkTheme ? 'light' : 'dark';
    this.applyTheme(nextTheme);
    localStorage.setItem(this.themeStorageKey, nextTheme);
  }

  private initializeTheme(): void {
    const savedTheme = localStorage.getItem(this.themeStorageKey);
    if (savedTheme === 'dark' || savedTheme === 'light') {
      this.applyTheme(savedTheme);
      return;
    }

    const prefersDark = window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches;
    this.applyTheme(prefersDark ? 'dark' : 'light');
  }

  private applyTheme(theme: 'light' | 'dark'): void {
    this.isDarkTheme = theme === 'dark';
    document.documentElement.setAttribute('data-theme', theme);
  }
}
