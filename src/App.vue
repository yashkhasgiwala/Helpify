<template>
  <div class="vue-tempalte">
   <mdb-container>
    <mdb-navbar  class="mt-2" hamburger navIconClass="icon-color" expand="xl">
      <mdb-navbar-brand>
        Helpify
      </mdb-navbar-brand>
      <mdb-navbar-toggler>
        <mdb-navbar-nav right>
          <mdb-nav-item href="/report" waves-fixed class="report-btn"><h6>Emergency Report</h6></mdb-nav-item>
          <mdb-nav-item href="/login" waves-fixed>Sign In</mdb-nav-item>
          <mdb-nav-item href="/" waves-fixed>Register Now!</mdb-nav-item>
          <mdb-nav-item href="/help" waves-fixed>Help</mdb-nav-item>
        </mdb-navbar-nav>
      </mdb-navbar-toggler>
    </mdb-navbar>
  
   
  </mdb-container>

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
<script>
  import { mdbNavbar, mdbNavItem, mdbNavbarNav, mdbNavbarToggler, mdbContainer, mdbNavbarBrand,} from 'mdbvue';
  export default {
    name: 'HamburgerMenuPage',
    components: {
      mdbNavbar,
      mdbNavItem,
      mdbNavbarNav,
      mdbNavbarToggler,
      mdbContainer,
      mdbNavbarBrand,
     
    }
  }
</script>
<style>
  .icon-color {
    color: #f2dcbb;
    
    
  }
</style>
