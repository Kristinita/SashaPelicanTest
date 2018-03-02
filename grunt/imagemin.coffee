module.exports =
	dynamic:
		options:
			optimizationLevel: 7
		files: [
			expand: true
			cwd: '.'
			src: ['output/images/**/*.{png,jpg,jpeg,gif,svg}']
			dest: '.'
			]