import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

import { Feedback as FeedbackService } from '../../services/feedback';
import { Navbar } from '../../components/navbar/navbar';

@Component({
  selector: 'app-feedback',
  standalone: true,
  imports: [CommonModule, FormsModule, Navbar],
  templateUrl: './feedback.html',
  styleUrl: './feedback.css',
})
export class Feedback {
  feedbackList: any[] = [];
  myEnrollments: any[] = [];
  selectedEnrollment: any = null;

  enrollment_id: number | null = null;
  faculty_id: number | null = null;
  rating: number | null = null;
  comments = '';

  message = '';
  errorMessage = '';

  constructor(private feedbackService: FeedbackService) {
    this.loadFeedback();
    this.loadMyEnrollments();
  }

  loadFeedback() {
    this.feedbackService.getFeedback().subscribe({
      next: (data) => {
        this.feedbackList = data;
      },
      error: () => {
        this.errorMessage = 'Failed to load feedback';
      }
    });
  }

  loadMyEnrollments() {
    this.feedbackService.getMyEnrollments().subscribe({
      next: (data) => {
        this.myEnrollments = data;
      },
      error: () => {
        this.errorMessage = 'Failed to load your enrollments';
      }
    });
  }

  onEnrollmentChange() {
    this.faculty_id = null;

    this.selectedEnrollment = this.myEnrollments.find(
      e => e.id == this.enrollment_id
    );
  }

  submitFeedback() {
    this.message = '';
    this.errorMessage = '';

    if (!this.enrollment_id || !this.faculty_id || !this.rating) {
      this.errorMessage = 'Enrollment, faculty and rating are required';
      return;
    }

    if (this.rating < 1 || this.rating > 5) {
      this.errorMessage = 'Rating must be between 1 and 5';
      return;
    }

    const data = {
      enrollment_id: this.enrollment_id,
      faculty_id: this.faculty_id,
      rating: this.rating,
      comments: this.comments
    };

    this.feedbackService.createFeedback(data).subscribe({
      next: () => {
        this.message = 'Feedback submitted successfully';

        this.enrollment_id = null;
        this.faculty_id = null;
        this.rating = null;
        this.comments = '';
        this.selectedEnrollment = null;

        this.loadFeedback();
      },
      error: (error) => {
        this.errorMessage = error.error?.error || 'Feedback submission failed';
      }
    });
  }
}