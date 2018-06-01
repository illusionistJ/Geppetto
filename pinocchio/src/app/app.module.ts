import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { MatNavList } from '@angular/material'


import { AppComponent } from './app.component';
import { MainModule } from './main/main.module';
import { UserModule } from './user/user.module';


@NgModule({
  declarations: [
    AppComponent
  ],
  imports: [
    BrowserModule,MatNavList,

    /* App Modules */
    MainModule, UserModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
