import { Component, OnInit } from '@angular/core';
import { DataService } from '../../services/data.service';
import { SearchedItem } from '../../models/SearchedItem';
import { Store } from '@ngrx/store';
import { State } from 'src/app/store/procuct.reducers';

@Component({
  selector: 'app-item-select',
  templateUrl: './item-select.component.html',
  styleUrls: ['./item-select.component.scss']
})
export class ItemSelectComponent implements OnInit {

  constructor(
    private dataService: DataService,
    private store: Store<{product: State}>
    ) { }

  item: SearchedItem;
  show: boolean = true;

  ngOnInit(): void {
    this.store.select(state => state.product.searchedItem).subscribe(
      data => {
        this.item = data;
        console.log('Got Data: ' + data.name);
      }
    )
  }

  hideComponent(){
    this.show = !this.show;
  }

}
