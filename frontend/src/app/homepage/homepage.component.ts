import { Component, OnInit } from '@angular/core';
import { FormControl, Validators } from '@angular/forms';

export class LoginBody {
  email: string = '';
  password: string = '';
}

@Component({
  selector: 'app-homepage',
  templateUrl: './homepage.component.html',
  styleUrls: ['./homepage.component.css']
})
export class HomepageComponent implements OnInit {
  constructor() {}

  ngOnInit(): void {}

  body = new LoginBody();
  async submit(){

  }
}
