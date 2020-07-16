import { Component } from '@angular/core';
import { DataService } from '../../services/data.service';
import { Store } from '@ngrx/store';
import { searchProduct } from '../../store/product.actions';
import { State } from '../../store/procuct.reducers';

@Component({
  selector: 'app-search-bar',
  templateUrl: './search-bar.component.html',
  styleUrls: ['./search-bar.component.scss']
})
export class SearchBarComponent{

  itemName: string = "Logitech-g920";
  constructor(
    private dataService: DataService,
    private store: Store<{product: State}>
    ) { }

  onSubmit(){
    this.store.dispatch(searchProduct({searchingPhrase: this.itemName}));
  }
}
