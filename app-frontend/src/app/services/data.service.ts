import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Item } from '../models/Item';
import { Observable } from 'rxjs';
import { Subject } from 'rxjs'

@Injectable({
  providedIn: 'root'
})
export class DataService {

  apiUrl: string = `http://${window.location.hostname}:5034/items?name=logitech-g920` //TODO: <-- hardcoded

  searchedItems: {};
  private itemSource = new Subject();
  itemContent$ = this.itemSource.asObservable();

  constructor(private http: HttpClient) { }

  shareItems(item: {}){
    this.itemSource.next(item);
  }

  getProposalItems(): Observable<Item> {
    return this.http.get<Item>(this.apiUrl);
  }

  getSingleItem(): Observable<Item> {
    return this.http.get<Item>(`${this.apiUrl}/items/item`);
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
