<template>
	<div class="vue-tempalte">
		<form>
			<h3>Report</h3>

			<div class="form-group">
				<label>Upload a picture of the accident: 
					<input type="file" name="img1" class="form-control">
				</label>
			</div>

			<div class="form-group">
				<label>Enter the Licence plate Number: 
					<input type="text" name="licencePlateNumber" class="form-control form-control-lg">
				</label>
			</div>


			<button type="submit" class="btn btn-dark btn-lg btn-block">Submit</button>

		</form>
	</div>
</template>

<script>
	export default {
		data() {
			return {}
		}
	}
</script>

