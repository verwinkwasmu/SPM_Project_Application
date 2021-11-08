<template>
    <header id="header" class="fixed-top">
      <div class="container d-flex align-items-center">
        <a href="/LearnerHomePage" class="logo me-auto"><img src="~/assets/img/LMS.png" alt="" class="img-fluid"> AIO Learning Management System </a>


        <nav id="navbar" class="navbar">
          <ul>
            <li>
                <a class="nav-link" href="/LearnerHomePage">Home</a>
            </li>
            
            <li>
                <a class="nav-link" href="/LearnerViewCourse">Enrol</a>
            </li>
            <li>
              <a href="/LearnerPersonalCourse">My courses</a>
            </li>

            <li class="dropdown">
              <a href="#"
                ><span>Profile</span> <i class="bi bi-chevron-down"></i
              ></a>
              <ul>
                <li><a href="/LearnerViewAllBadges">My Badges</a></li>
                <li><a href="/">Logout</a></li>
              </ul>
            </li>

          </ul>
          <i class="bi bi-list mobile-nav-toggle"></i>
        </nav>
      </div>
    </header>
</template>