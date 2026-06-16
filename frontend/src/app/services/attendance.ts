import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';
import { environment } from '../../environments/environment';

@Injectable({
  providedIn: 'root',
})
export class Attendance {
  private apiUrl = environment.apiUrl + '/attendance';
  private enrollmentsUrl = environment.apiUrl + '/enrollments';

  constructor(private http: HttpClient) {}

  private getHeaders() {
    const token = localStorage.getItem('token');

    return {
      headers: new HttpHeaders({
        Authorization: `Bearer ${token}`
      })
    };
  }

  getAttendance(): Observable<any[]> {
    return this.http.get<any[]>(`${this.apiUrl}/`, this.getHeaders());
  }

  markAttendance(data: any): Observable<any> {
    return this.http.post(`${this.apiUrl}/`, data, this.getHeaders());
  }

  getEnrollments(): Observable<any[]> {
    return this.http.get<any[]>(
      `${this.enrollmentsUrl}/`,
      this.getHeaders()
    );
  }
}