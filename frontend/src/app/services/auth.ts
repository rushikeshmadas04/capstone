import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { environment } from '../../environments/environment';

@Injectable({
  providedIn: 'root',
})
export class Auth {
  private apiUrl = environment.apiUrl + '/auth';

  constructor(private http: HttpClient) {}

  login(data: any): Observable<any> {
  return this.http.post(`${this.apiUrl}/login`, data);
}

register(data: any): Observable<any> {
  return this.http.post(`${this.apiUrl}/register`, data);
}

  saveLoginData(response: any): void {
    localStorage.setItem('token', response.access_token);
    localStorage.setItem('user', JSON.stringify(response.user));
    localStorage.setItem('role', response.user.role);
  }

  getRole(): string | null {
    return localStorage.getItem('role');
  }

  logout(): void {
    localStorage.clear();
  }
}