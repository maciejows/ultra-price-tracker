import { Component, OnInit } from '@angular/core';
import { DataService } from '../../services/data.service';
import { SearchedItem } from '../../models/SearchedItem';
import { searchProduct } from '../../store/product.actions';
import { Store } from '@ngrx/store';
import { State } from 'src/app/store/procuct.reducers';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-item-select',
  templateUrl: './item-select.component.html',
  styleUrls: ['./item-select.component.scss']
})
export class ItemSelectComponent implements OnInit {
  item: SearchedItem;
  searchQuery: string;

  constructor(
    private dataService: DataService,
    private route: ActivatedRoute,
    private store: Store<{product: State}>
    ) { 
      this.store.select(state => state.product.searchedItem).subscribe(
        data => {
          this.item = data;
          console.log('Got Data: ' + data.name);
        }
      )
    }

  ngOnInit(): void {
    this.route.queryParams.subscribe(params => {
      this.searchQuery = params['name'];
      this.store.dispatch(searchProduct({searchingPhrase: this.searchQuery}));
    })
  }

}
