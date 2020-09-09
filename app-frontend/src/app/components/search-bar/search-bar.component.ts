import { Component, OnInit, OnDestroy } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { Subscription } from 'rxjs';

@Component({
  selector: 'app-search-bar',
  templateUrl: './search-bar.component.html',
  styleUrls: ['./search-bar.component.scss']
})
export class SearchBarComponent{
  itemName: string;
  
  constructor(private router: Router) { }
  
  onSubmit(): void {
    this.router.navigate(['item'], {queryParams: {name: this.itemName}});
    this.itemName = '';
  }
}
