import { Component, OnInit } from '@angular/core';
import { DataService } from '../../services/data.service';
import { Subscription } from 'rxjs';

@Component({
  selector: 'app-item-select',
  templateUrl: './item-select.component.html',
  styleUrls: ['./item-select.component.scss']
})
export class ItemSelectComponent implements OnInit {

  constructor(private dataService: DataService) { }

  items: {name: string, price: number, thumbnail: string};
  show: boolean;

  ngOnInit(): void {
    this.dataService.itemContent$.subscribe( data =>  {
      this.show = true;
      this.items = data as {name: string, price: number, thumbnail: string}
    });
  }

  hideComponent(){
    this.show = !this.show;
  }

}
