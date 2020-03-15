<template>
  <b-container fluid>
    <div id="app">
      <!-- set progressbar -->
      <vue-progress-bar></vue-progress-bar>
      <!-- NAV BAR ROW -->
      <!-- <b-row>
        <div class="w-100 mb-3">
          <b-navbar toggleable="lg" type="dark" variant="dark">
            <b-navbar-brand href="#">Automated paper correction (alpha)</b-navbar-brand>
            <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
      <b-collapse id="nav-collapse" is-nav>-->
      <!-- Right aligned nav items -->
      <!-- <b-navbar-nav class="ml-auto">
                <b-nav-item>Docs</b-nav-item>
                <b-nav-item>About</b-nav-item>
              </b-navbar-nav>
            </b-collapse>
          </b-navbar>
        </div>
      </b-row>-->
      <router-view></router-view>
    </div>
  </b-container>
</template>
<script></script>
<style>
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  position: absolute;
  left: 0;
  right: 0;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
