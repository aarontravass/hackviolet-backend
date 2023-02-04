import { HttpClient, HttpErrorResponse } from "@angular/common/http";
import { Injectable } from "@angular/core";
import { Observable, throwError } from "rxjs";
import { catchError } from "rxjs/operators";
import { LoginBody } from "../homepage/homepage.component";

@Injectable({
    providedIn: 'root'
})
export class LoginService{
    constructor(private readonly http:HttpClient){

    }

    private handleError(error: HttpErrorResponse) {
        return throwError(error);
    }




    login(body: LoginBody):Observable<any>{
        return this.http.post('', body).pipe(catchError(this.handleError));;
    }
}