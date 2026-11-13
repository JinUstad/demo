import React, { useEffect, useState } from "react";
import { NavLink } from "react-router-dom";

function ImageSlider() {

    // first step is create use state for the store and get value for the api data
    const [users, setUsers] = useState([]);
    const [singlepost, setSinglePost] = useState();

    // useEffect(() => {
    //     alert("ImageSlider component mounted");
    // },[])

    // second step get the api data using fetch and store the data in the use state.


    useEffect(() => {

        // fetch method we can call the api..
        fetch("https://jsonplaceholder.typicode.com/users")

            // when we use then method we get the promise and response from the api .
            .then((response) => response.json())
            .then((data) => {

                console.log("users:", data);

                // setUsers means we store the api data...
                setUsers(data);
            })

            // if we get any error show in cath method.
            .catch((error) => {
                console.log("Error:", error);
            });
    }, []);



    useEffect(() => {
        fetch("https://jsonplaceholder.typicode.com/posts/1")
            .then((res) => res.json())
            .then((singlepost) => {
                console.log("singlepost:", singlepost);
                setSinglePost(singlepost);
            })
            .catch((error) => {
                console.log("Error:", error);
            })
    }, [])

    return (
        <div className="container py-5">

            <NavLink to="/services">
                Servies
            </NavLink>
            <h1>Users List</h1>


            {/* jsx means javascript in html */}

            {/* <div className="row ">

                {users.map((users) => (

                    <div className="col-lg-4 card mb-3" key={users.id}>
                        <div className="card-body">
                            <h3 className="card-title">{users.name}</h3>
                            <p className="card-text">{users.email}</p>
                            <p className="card-text">{users.phone}</p>
                        </div>
                    </div>
                ))}
            </div> */}

            <h1>Single Post------------------</h1>
            <h1>{singlepost?.id}</h1>
            <p>{singlepost?.title}</p>
            <small>{singlepost?.body}</small>
        </div>
    );
}

export default ImageSlider;