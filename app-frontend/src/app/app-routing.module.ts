import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { ItemSelectComponent } from './components/item-select/item-select.component';

const routes: Routes = [
  { path: 'search', component: ItemSelectComponent },
  { path: '**', redirectTo: '/' } 
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
