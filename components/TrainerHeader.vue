<template>
    <header id="header" class="fixed-top">
      <div class="container d-flex align-items-center">
        <a href="/TrainerHomePage" class="logo me-auto"><img src="~/assets/img/LMS.png" alt="" class="img-fluid"> AIO Learning Management System </a>
        <!-- <h3 class="logo me-auto"><a to="/">AIO Learning Management System</a></h3> -->
        <!-- Uncomment below if you prefer to use an image logo -->
        

        <nav id="navbar" class="navbar">
          <ul>
            <li>
                <a class="nav-link scrollto active" href="/">Home</a>
            </li>
            <!--<li><a class="nav-link scrollto" href="#about">About</a></li>-->
            <!--<li><a class="nav-link scrollto" href="#services">Services</a></li>-->
            <!--<li>
              <a class="nav-link scrollto" href="#portfolio">Portfolio</a>
            </li>-->
            <!--<li><a class="nav-link scrollto" href="#team">Team</a></li>-->
            <li class="dropdown">
              <a href="TrainerViewCourses"
                ><span>View Teaching Courses</span> <i class="bi bi-chevron-down"></i
              ></a>
              <ul>
                <li><a href="#">Course 1</a></li>
                <!-- <li class="dropdown">
                  <a href="#"
                    ><span>Deep Drop Down</span>
                    <i class="bi bi-chevron-right"></i
                  ></a>
                  <ul>
                    <li><a href="#">Deep Drop Down 1</a></li>
                    <li><a href="#">Deep Drop Down 2</a></li>
                    <li><a href="#">Deep Drop Down 3</a></li>
                    <li><a href="#">Deep Drop Down 4</a></li>
                    <li><a href="#">Deep Drop Down 5</a></li>
                  </ul>
                </li> -->
                <li><a href="#">Course 2</a></li>
                <li><a href="#">Course 3</a></li>
                <li><a href="#">Course 4</a></li>
              </ul>
            </li>
            <li>
                <a class="nav-link" href="/">Forum</a>
            </li>
            <li class="dropdown">
              <a href="#"
                ><span>User</span> <i class="bi bi-chevron-down"></i
              ></a>
              <ul>
                <li><a href="#">Profile</a></li>
                <li><a href="#">Logout</a></li>
              </ul>
            </li>
            <!--<li><a class="nav-link scrollto" href="#contact">Contact</a></li> -->
            <!--<li>
              <a class="getstarted scrollto" href="/login">HR1</a>
              <a class="getstarted scrollto" href="/register">Register</a> 
            </li> -->
          </ul>
          <i class="bi bi-list mobile-nav-toggle"></i>
        </nav>
        <!-- .navbar -->
      </div>
    </header>
    <!-- End Header -->
</template>