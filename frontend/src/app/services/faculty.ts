import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';
import { environment } from '../../environments/environments';

@Injectable({
  providedIn: 'root',
})
export class Faculty {
  private apiUrl = environment.apiUrl + '/faculties';
  private skillsUrl = environment.apiUrl + '/skills';

  constructor(private http: HttpClient) {}

  private getHeaders() {
    const token = localStorage.getItem('token');

    return {
      headers: new HttpHeaders({
        Authorization: `Bearer ${token}`
      })
    };
  }

  getFaculties(): Observable<any[]> {
    return this.http.get<any[]>(`${this.apiUrl}/`, this.getHeaders());
  }

  createFaculty(data: any): Observable<any> {
    return this.http.post(`${this.apiUrl}/`, data, this.getHeaders());
  }

  updateFaculty(id: number, data: any): Observable<any> {
    return this.http.put(`${this.apiUrl}/${id}`, data, this.getHeaders());
  }

  deleteFaculty(id: number): Observable<any> {
    return this.http.delete(`${this.apiUrl}/${id}`, this.getHeaders());
  }

  getSkills(): Observable<any[]> {
    return this.http.get<any[]>(
      `${this.skillsUrl}/`,
      this.getHeaders()
    );
  }

  createSkill(data: any): Observable<any> {
    return this.http.post(
      `${this.skillsUrl}/`,
      data,
      this.getHeaders()
    );
  }

  assignSkill(facultyId: number, skillId: number): Observable<any> {
    return this.http.post(
      `${this.apiUrl}/${facultyId}/skills/${skillId}`,
      {},
      this.getHeaders()
    );
  }

  searchBySkill(skill: string): Observable<any[]> {
    return this.http.get<any[]>(
      `${this.apiUrl}/search?skill=${skill}`,
      this.getHeaders()
    );
  }
}