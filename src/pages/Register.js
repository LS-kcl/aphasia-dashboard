// Import the react JS packages 
import axios from "axios";
import {useState} from "react";// Define the Login function.
import { setAuthToken } from "../helpers/setAuthToken()";
axios.defaults.withCredentials = true;

export const SignUp = () => {
		const [username, setUsername] = useState('');
		const [email, setEmail] = useState('');
		const [password, setPassword] = useState('');
		// Create the submit method.
		const submit = async e => {
				e.preventDefault();
				
				const user = {
						username: username,
						email: email,
						password: password
				};

				axios.post('api/sign_up', user).then(res => {
						// On resolution of login
						const token = res.data.access; // NB: Token is returned under "access"

						// Store locally & set token to axios common header
						localStorage.setItem('token', token);
						setAuthToken(token);

						// Redirect to homepage
						window.location.href = '/'
				}).catch(
						// On error, log
						err => console.log(err)
				)

		}
				
		return(
		<div className="col-sm-12 col-md-6 offset-md-3">
			<form onSubmit={submit}>
				<h1 className="text-white">Sign Up</h1>
				<div className="form-group mt-3">
					<label className="text-white">Username</label>
					<input className="form-control mt-1" 
						placeholder="Enter Username" 
						name='username'  
						type='text' value={username}
						required 
						onChange={e => setUsername(e.target.value)}/>
				</div>
				<div className="form-group mt-3">
					<label className="text-white">Email</label>
					<input className="form-control mt-1" 
						placeholder="Enter Email" 
						name='email'  
						type='text' value={email}
						required 
						onChange={e => setEmail(e.target.value)}/>
				</div>
				<div className="form-group mt-3">
					<label className="text-white">Password</label>
					<input name='password' 
						type="password"     
						className="form-control mt-1"
						placeholder="Enter password"
						value={password}
						required
						onChange={e => setPassword(e.target.value)}/>
				</div>
				<div className="d-grid gap-2 mt-3">
					<button type="submit" 
						 className="btn btn-light">Submit</button>
				</div>
			</form>
		 </div>
		 )
}