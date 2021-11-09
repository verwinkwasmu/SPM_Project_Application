<template>
  <b-modal id="my-modal" hide-footer title="You passed the quiz!">
    <div class="d-block text-center">
      <h3>Congratulations!</h3>
      <p>Woohoo! You have completed this course!</p>
      <div class="col-lg-12 badge">
        <img
          src="~/assets/img/badge.png"
          class="img-fluid animated"
          alt=""
          width="200px"
          length="200px"
        />
      </div>
    </div>
    <b-button
      class="mt-2"
      variant="outline-success"
      block
      href="/LearnerViewCourse"
      >View other available courses</b-button
    >
  </b-modal>
</template>