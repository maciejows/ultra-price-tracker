import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';

@Component({
  selector: 'app-search-bar',
  templateUrl: './search-bar.component.html',
  styleUrls: ['./search-bar.component.scss']
})
export class SearchBarComponent implements OnInit{
  itemName: string;

  constructor(
    private route: ActivatedRoute,
    private router: Router,
    ) { }

  ngOnInit(): void {
    this.route.queryParams.subscribe(
      params => {
        this.itemName=params['name'];
      }
    )
  }
  
  onSubmit(): void {
    this.router.navigate(['search'], {queryParams: {name: this.itemName}});
  }
}
