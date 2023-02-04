import { HttpErrorResponse } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';
import { FormControl, Validators } from '@angular/forms';
import { AuthService } from '../services/auth.service';

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
    constructor(private readonly authService: AuthService) { }

    ngOnInit(): void { }

    body = new LoginBody();
    async submit() {
        await this.authService.login(this.body).toPromise().then(res => {

        }).catch((error: HttpErrorResponse) => {

        })
    }
}
