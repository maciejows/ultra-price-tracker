import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { ItemDisplayComponent } from './components/item-display/item-display.component';

const routes: Routes = [
  { path: 'item', component: ItemDisplayComponent },
  { path: '**', redirectTo: '/' } 
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
