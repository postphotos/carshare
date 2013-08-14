#!/usr/bin/python
from csv import DictReader

the_file = DictReader(open('carshare.csv','rU'), dialect="excel")
for row in the_file:
  string = """
  <div class="row">
				<div class="large-4 columns">
				<!-- iframe --> &nbsp;
				</div>
			
				<div class="large-8 columns">
						<h4>Sample trip: {title}</h4>
						<p>{details}</p>

							<div class="row">
								<div class="small-4 columns panel first">
									<h5>First place: {fname}</h5>
									<p class="n">{fmath}</p>
									<hr>
									<p class="n">{ffinal}</p>
								</div>

								<div class="small-4 columns panel">
									<h5>Second place: {sname}</h5>
									<p class="n">{smath}</p>
									<hr>
									<p class="n">{sfinal}</p>
								</div>

							
								<div class="small-4 columns panel third">
									<h5>Third place: {tname}</h5>
									<p class="n">{tmath}</p>
									<hr>
									<p class="n">{tfinal}</p>
								</div>

				</div>
		</div><hr>""".format(**row)
  print string