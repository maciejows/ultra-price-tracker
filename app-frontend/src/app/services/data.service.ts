import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { SearchedItem } from '../models/SearchedItem';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class DataService {

  apiUrl: string = `http://${window.location.hostname}:5034/items`

  constructor(private http: HttpClient) { }

  getProposalItems(itemName: string): Observable<SearchedItem> {
    return this.http.get<SearchedItem>(`${this.apiUrl}?name=${itemName}`);
  }

  getSingleItem(): Observable<SearchedItem> {
    return this.http.get<SearchedItem>(`${this.apiUrl}/items/item`);
  }

  slugify(text: string): string {
    const a = 'àáâäæãåāăąçćčđďèéêëēėęěğǵḧîïíīįìłḿñńǹňôöòóœøōõőṕŕřßśšşșťțûüùúūǘůűųẃẍÿýžźż·/_,:;'
    const b = 'aaaaaaaaaacccddeeeeeeeegghiiiiiilmnnnnoooooooooprrsssssttuuuuuuuuuwxyyzzz------'
    const p = new RegExp(a.split('').join('|'), 'g')

    return text.toString().toLowerCase()
      .replace(/\s+/g, '-') // Replace spaces with -
      .replace(p, c => b.charAt(a.indexOf(c))) // Replace special characters
      .replace(/&/g, '-and-') // Replace & with 'and'
      .replace(/[^\w\-]+/g, '') // Remove all non-word characters
      .replace(/\-\-+/g, '-') // Replace multiple - with single -
      .replace(/^-+/, '') // Trim - from start of text
      .replace(/-+$/, '') // Trim - from end of text
  }

}
