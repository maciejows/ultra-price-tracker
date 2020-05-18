import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Item } from '../models/item';

@Injectable({
  providedIn: 'root'
})
export class DataService {

  apiUrl: string = "http://127.0.0.1:5034"

  constructor(private http: HttpClient) { }

  getProposalItems(): Observable<Item> {
    return this.http.get<Item>(this.apiUrl);
  }

  getSingleItem(): Observable<Item> {
    return this.http.get<Item>(`${this.apiUrl}/item`);
  }
}
