import { HttpErrorResponse } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';
import { AuthService } from '../services/auth.service';


export class RegistrationBody {
    email: string = '';
    password: string = '';
    first_name: string = '';
    last_name: string = '';
}
@Component({
    selector: 'app-registration',
    templateUrl: './registration.component.html',
    styleUrls: ['./registration.component.css']
})
export class RegistrationComponent implements OnInit {

    constructor(private readonly authService: AuthService) { }
    body: RegistrationBody = new RegistrationBody();
    ngOnInit(): void {
    }

    async submit() {
        await this.authService.register(this.body).toPromise().then(res => {

        }).catch((error: HttpErrorResponse) => {

        })
    }

}
