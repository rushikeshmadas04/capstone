import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';
import { environment } from '../../environments/environments';

@Injectable({
  providedIn: 'root',
})
export class Enrollment {
  private apiUrl = environment.apiUrl + '/enrollments';
  private studentsUrl = environment.apiUrl + '/students';
  private programsUrl = environment.apiUrl + '/programs';

  constructor(private http: HttpClient) {}

  private getHeaders() {
    const token = localStorage.getItem('token');

    return {
      headers: new HttpHeaders({
        Authorization: `Bearer ${token}`
      })
    };
  }

  getEnrollments(): Observable<any[]> {
    return this.http.get<any[]>(`${this.apiUrl}/`, this.getHeaders());
  }

  createEnrollment(data: any): Observable<any> {
    return this.http.post(`${this.apiUrl}/`, data, this.getHeaders());
  }

  deleteEnrollment(id: number): Observable<any> {
    return this.http.delete(`${this.apiUrl}/${id}`, this.getHeaders());
  }

  getStudents(): Observable<any[]> {
    return this.http.get<any[]>(
      `${this.studentsUrl}/`,
      this.getHeaders()
    );
  }

  getPrograms(): Observable<any[]> {
    return this.http.get<any[]>(
      `${this.programsUrl}/`,
      this.getHeaders()
    );
  }
}