import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';
import { environment } from '../../environments/environments';

@Injectable({
  providedIn: 'root',
})
export class Feedback {
  private apiUrl = environment.apiUrl + '/feedbacks';
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

  getFeedback(): Observable<any> {
    return this.http.get(`${this.apiUrl}/`, this.getHeaders());
  }

  createFeedback(data: any): Observable<any> {
    return this.http.post(`${this.apiUrl}/`, data, this.getHeaders());
  }

  getFacultyRating(facultyId: number): Observable<any> {
    return this.http.get(
      `${this.apiUrl}/faculty/${facultyId}/rating`,
      this.getHeaders()
    );
  }

  getMyEnrollments(): Observable<any> {
  return this.http.get(
    `${this.enrollmentsUrl}/my`,
    this.getHeaders()
  );
}
}