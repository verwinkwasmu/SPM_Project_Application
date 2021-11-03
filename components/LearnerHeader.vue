<template>
    <header id="header" class="fixed-top">
      <div class="container d-flex align-items-center">
        <a href="/LearnerHomePage" class="logo me-auto"><img src="~/assets/img/LMS.png" alt="" class="img-fluid"> AIO Learning Management System </a>


        <nav id="navbar" class="navbar">
          <ul>
            <li>
                <a class="nav-link scrollto active" href="/">Home</a>
            </li>
            
            <li>
                <a class="nav-link" href="LearnerViewAvailableCourses">Enrol</a>
            </li>
            <li class="dropdown">
              <a href="TrainerViewCourses"
                ><span>My courses</span> <i class="bi bi-chevron-down"></i
              ></a>
              <ul>
                <li><a href="#">Course 1</a></li>
                <li><a href="#">Course 2</a></li>
                <li><a href="#">Course 3</a></li>
                <li><a href="#">Course 4</a></li>
              </ul>
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

          </ul>
          <i class="bi bi-list mobile-nav-toggle"></i>
        </nav>
      </div>
    </header>
</template>