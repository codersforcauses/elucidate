<template>
  <div>
    <div class="container pl-20 mx-auto">
      <!-- Section 1 -->
      <div class="grid items-center lg:grid-cols-2 gap-x-12 mt-36 mb-52">
        <div>
          <h1 class="mb-10 text-6xl leading-snug text-black-400">
            What do you want <br />to learn today?
          </h1>
          <!-- Search bar -->
          <SearchBar />
          <!-- 'I already have acc' button which directs user to the log in page -->
          <haveAccBtn />
          <nuxt-img src="shapes.svg" class="mt-5 justify-self-start" />
        </div>
        <div>
          <nuxt-img src="QAimage.png" />
        </div>
      </div>
    </div>
    <!-- Section 2 (sneak-peak of the quizzes) -->
    <div class="pt-20 pb-40 bg-indigo-500">
      <h2 class="py-20 text-5xl text-center text-white">Look at our quizzes</h2>
      <div
        class="grid gap-5 mx-10 md:grid-cols-2 xl:gap-14 2xl:grid-cols-3 xl:mx-32 3xl:mx-48 content-evenly"
      >
        <QuizCard />
        <QuizCard />
        <QuizCard />
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'IndexPage',
};
</script>
