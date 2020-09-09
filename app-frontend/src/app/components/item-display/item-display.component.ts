import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { Subscription, Observable } from 'rxjs';
import { Store } from '@ngrx/store';
import { ItemState } from 'src/app/models/ItemState';
import { searchItem } from '../../store/product.actions';
import { Item } from 'src/app/models/Item';

import { ChartDataSets } from 'chart.js';
import { Color, Label } from 'ng2-charts';

@Component({
  selector: 'app-item-display',
  templateUrl: './item-display.component.html',
  styleUrls: ['./item-display.component.scss']
})
export class ItemDisplayComponent implements OnInit {

  routeSub: Subscription;
  item$: Observable<Item>;
  error$: Observable<string>;

  public barChartOptions = {
    scaleShowVerticalLines: false,
    responsive: true
  };

  public lineChartData: ChartDataSets[] = [
    { data: [65, 59, 80, 81, 56, 55, 40], label: 'Price' },
  ];
  public lineChartLabels: Label[] = ['January', 'February', 'March', 'April', 'May', 'June', 'July'];
  public lineChartOptions: any = {
    responsive: true,
  };
  public lineChartColors: Color[] = [
    {
      borderColor: '#f57f17',
      backgroundColor: 'rgba(255,0,0,0)',
    },
  ];
  public lineChartLegend = true;
  public lineChartType = 'line';
  public lineChartPlugins = [];

  constructor(
    private route: ActivatedRoute,
    private store: Store<{itemState: ItemState}>
    ) { 
     
    }

  ngOnInit(): void {
    this.routeSub = this.route.queryParams.subscribe(
      params => {
        this.store.dispatch(searchItem({searchingPhrase: params['name']}))
      }
    )

    this.item$ = this.store.select(state=> state.itemState.item);
    this.error$ = this.store.select(state=> state.itemState.error); 
  }

  ngOnDestroy(): void {
    this.routeSub.unsubscribe();
  }

}
