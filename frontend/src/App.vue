<template>
  <div>
    <h1>Твой умный блог™</h1>
    <nav class="main_header">
      <!-- if this is the link that we are at, display it in black. (default is green-ish) -->
      <router-link to="/">Домой</router-link> |
      <router-link to="/blog/create">Создать публикацию</router-link>

      <!-- <router-link to="/">Домой</router-link> | -->
      <!-- <router-link to="/blog/create">Создать публикацию</router-link> -->
    </nav>
    <div class="main_background"></div>

    <div class="content_class">
      <div class="content_block">
        <router-view />
      </div>
    </div>
    <!-- my contacts at the bottom -->
    <footer>
      <div class="footer_content">
        <div class="footer_content_block">
          <h3>My Contacts</h3>
          <a href="https://khrmff.ru">My Website</a> |
          <a href="https://github.com/verybigsad">My GitHub</a> |
          <a href="https://t.me/mikhail_khromov">My Telegram</a>
        </div>
      </div>
    </footer>
  </div>
</template>

<script>
export default {
  name: "App",
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

.main_header {
  font-size: 1.2rem;
}

.main_header a {
  color: #42b983;
}

footer {
  background-color: #333;
  color: white;
  padding: 10px;
  margin-top: 10px;
  /* make footer sticky */
  position: fixed;
  bottom: 0;
  left: 0;
  width: 100%;
}

footer a {
  color: white;
}

.footer_content {
  display: flex;
  justify-content: center;
}


</style>
