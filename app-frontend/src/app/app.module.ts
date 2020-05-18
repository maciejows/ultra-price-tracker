import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { MDBBootstrapModule } from 'angular-bootstrap-md';
import { HttpClientModule } from '@angular/common/http';
import { AppRoutingModule } from './app-routing.module';
import { FormsModule } from '@angular/forms';
import { AppComponent } from './app.component';
import { NavbarComponent } from './components/navbar/navbar.component';
import { SearchBarComponent } from './components/search-bar/search-bar.component';

@NgModule({
  declarations: [
    AppComponent,
    NavbarComponent,
    SearchBarComponent
  ],
  imports: [
    BrowserModule,
    MDBBootstrapModule.forRoot(),
    AppRoutingModule,
    HttpClientModule,
    FormsModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
