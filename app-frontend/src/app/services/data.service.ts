import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class DataService {

  apiUrl: string = "Any url"

  constructor(private http: HttpClient) { }

  getProposalItems(): Observable<any> {
    return this.http.get<any>(this.apiUrl);
  }

  getSingleItem(): Observable<any> {
    return this.http.get<any>(this.apiUrl);
  }
}
