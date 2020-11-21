<template>
  <div class="vue-tempalte">
    <!-- Navigation -->
    <nav class="navbar shadow bg-white rounded justify-content-between flex-nowrap flex-row fixed-top">
      <div class="container">
        <a class="navbar-brand float-left" href="" >
           Helpify
        </a>
        <ul class="nav navbar-nav flex-row float-right">
			<li class="nav-item">
				<router-link class="btn btn-danger" to="/report" style="margin-right: 20px;">Emergency Report</router-link>
			</li>

			<li class="nav-item">
				<router-link class="nav-link pr-3" to="/login">Sign in</router-link>
			</li>

			<li class="nav-item">
				<router-link class="nav-link pr-3" to="/">Register Now!</router-link>
			</li>

			<li class="nav-item">
				<router-link class="nav-link pr-3" to="/">Help</router-link>
			</li>

		  
        </ul>
      </div>
    </nav>

    <!-- Main -->
    <div class="App">
      <div class="vertical-center">
        <div class="inner-block">
          <router-view />
        </div>
      </div>
    </div>
  </div>
</template>