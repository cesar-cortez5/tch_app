<!-- The navigation bar at the top of the page -->
<template>
    <div class="navdiv">
        <!-- This navbar design is copied from bootstrap -->
        <nav class="navbar navbar-expand-lg navbar-light bg-light" style="background-color: #e3f2fd;">
            <a class="navbar-brand">The Computer Hospital</a>
            <button
                class="navbar-toggler"
                type="button"
                data-toggle="collapse"
                data-target="#navbarNavAltMarkup"
                aria-controls="navbarNavAltMarkup"
                aria-expanded="false"
                aria-label="Toggle navigation"
            >
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNavAltMarkup">
                <div class="navbar-nav">
                    <!-- If you want to create a new button, copy one of these bottom codes, but with the name of your page instead
                    eg. <router-link to ="/test_page" class="nav-item nav-link">Test Page </router_link>-->
                    <router-link to="/" class="nav-item nav-link active">
                        Home
                    </router-link>
                    <router-link to="/login" class="nav-item nav-link">Employee Login</router-link>
                    <router-link to="/admin_options" class="nav-item nav-link">Admin</router-link>
                </div>
            </div>
        </nav>
    </div>
</template>
