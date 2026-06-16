import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';
import { environment } from '../../environments/environments';

@Injectable({
  providedIn: 'root',
})
export class Student {
  private apiUrl = environment.apiUrl + '/students';
  private coursesUrl = environment.apiUrl + '/courses';

  constructor(private http: HttpClient) {}

  private getHeaders() {
    const token = localStorage.getItem('token');

    return {
      headers: new HttpHeaders({
        Authorization: `Bearer ${token}`
      })
    };
  }

  getStudents(): Observable<any[]> {
    return this.http.get<any[]>(`${this.apiUrl}/`, this.getHeaders());
  }

  createStudent(data: any): Observable<any> {
    return this.http.post(`${this.apiUrl}/`, data, this.getHeaders());
  }

  updateStudent(id: number, data: any): Observable<any> {
  return this.http.put(
    `${this.apiUrl}/${id}`,
    data,
    this.getHeaders()
  );
}

deleteStudent(id: number): Observable<any> {
  return this.http.delete(
    `${this.apiUrl}/${id}`,
    this.getHeaders()
  );
}

  getCourses(): Observable<any[]> {
    return this.http.get<any[]>(
      `${this.coursesUrl}/`,
      this.getHeaders()
    );
  }
}