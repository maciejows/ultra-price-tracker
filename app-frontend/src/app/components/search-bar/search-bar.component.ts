import { Component } from '@angular/core';
import { DataService } from '../../services/data.service';

@Component({
  selector: 'app-search-bar',
  templateUrl: './search-bar.component.html',
  styleUrls: ['./search-bar.component.scss']
})
export class SearchBarComponent{

  items: {};
  itemName: string = "Logitech g920";
  constructor(private dataService: DataService) { }

  onSubmit(){
    this.dataService.getProposalItems().subscribe(
      (data) => {
        this.items = data;
        console.log(this.items);
      });
  }
}
