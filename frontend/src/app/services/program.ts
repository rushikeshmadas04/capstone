import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';
import { environment } from '../../environments/environments';

@Injectable({
  providedIn: 'root',
})
export class Program {
  private apiUrl = environment.apiUrl + '/programs';
  private coursesUrl = environment.apiUrl + '/courses';
  private usersUrl = environment.apiUrl + '/users';
  private facultiesUrl = environment.apiUrl + '/faculties';

  constructor(private http: HttpClient) {}

  private getHeaders() {
    const token = localStorage.getItem('token');

    return {
      headers: new HttpHeaders({
        Authorization: `Bearer ${token}`
      })
    };
  }

  getPrograms(): Observable<any[]> {
    return this.http.get<any[]>(`${this.apiUrl}/`, this.getHeaders());
  }

  createProgram(data: any): Observable<any> {
    return this.http.post(`${this.apiUrl}/`, data, this.getHeaders());
  }

  updateProgram(id: number, data: any): Observable<any> {
    return this.http.put(`${this.apiUrl}/${id}`, data, this.getHeaders());
  }

  cancelProgram(id: number): Observable<any> {
    return this.http.put(`${this.apiUrl}/${id}/cancel`, {}, this.getHeaders());
  }

  deleteProgram(id: number): Observable<any> {
    return this.http.delete(`${this.apiUrl}/${id}`, this.getHeaders());
  }

  assignFaculty(programId: number, facultyId: number): Observable<any> {
    return this.http.post(
      `${this.apiUrl}/${programId}/faculty/${facultyId}`,
      {},
      this.getHeaders()
    );
  }

  getCourses(): Observable<any[]> {
    return this.http.get<any[]>(
      `${this.coursesUrl}/`,
      this.getHeaders()
    );
  }

  getCoordinators(): Observable<any[]> {
    return this.http.get<any[]>(
      `${this.usersUrl}/?role=COORDINATOR`,
      this.getHeaders()
    );
  }

  getFaculties(): Observable<any[]> {
    return this.http.get<any[]>(
      `${this.facultiesUrl}/`,
      this.getHeaders()
    );
  }
}