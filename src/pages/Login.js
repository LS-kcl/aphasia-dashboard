// Import the react JS packages 
import axios from "axios";
import {useState} from "react";// Define the Login function.
import { setAuthToken } from "../helpers/setAuthToken()";
axios.defaults.withCredentials = true;

export const Login = () => {
		const [username, setUsername] = useState('');
		const [password, setPassword] = useState('');
		// Create the submit method.
		const submit = async e => {
				e.preventDefault();
				
				const user = {
						username: username,
						password: password
				};

				axios.post('token/', user).then(res => {
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
		<div>
			<form className="Auth-form" onSubmit={submit}>
					<div className="Auth-form-content">
						<h1 className="Auth-form-title text-white">Sign In</h1>
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
					</div>
			</form>
		 </div>
		 )
}