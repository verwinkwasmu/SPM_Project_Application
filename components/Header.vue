<template>
    <header id="header" class="fixed-top">
      <div class="container d-flex align-items-center">
        <a href="/ViewCourses" class="logo me-auto"><img src="~/assets/img/LMS.png" alt="" class="img-fluid"> AIO Learning Management System </a>
        
        <nav id="navbar" class="navbar">
          <ul>
            <li>
                <a class="nav-link" href="/HRHomePage">Home</a>
            </li>
            <li class="dropdown">
              <a href="/ViewCourses"
                ><span>Courses</span></a>
            </li>
            <li>
              <a class="nav-link" href="/">Logout</a>
            </li>
           
          </ul>
          <i class="bi bi-list mobile-nav-toggle"></i>
        </nav>
      </div>
    </header>
</template>