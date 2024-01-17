# Load More from Database

A `Customer` list is stored in a SQLite database.
Upon a click on the load more button, an HTMX page reads more customers from the database.

<img src=../image/hx02-202401180439.gif width="600px">

# Updating two elements

Since the app placed the `Load more` button outside of the table, 
I could not use the way this ["Click to Load"](https://htmx.org/examples/click-to-load/) example shows.
For HTMX, updating multiple elements is doable.
However, it seems more challenging than updating a single element.
I followed the hx-swap-oob(Out of Band Responses) example.

In this example, not only the element "hx-target" points to but also the `bluebutton` itself has to be updated. 

```
      <button class="..." hx-get="..." hx-target="..." hx-swap="..." hx-trigger="load, click"
        id="bluebutton" hx-swap-oob="outerHTML:#bluebutton"> Load More
      </button>
```

htmx.config.useTemplateFragments needed to be set to true as:

```
  <meta name="htmx-config" content='{"useTemplateFragments":"true"}'>
```

Refs:
1. [Updating Other Content](https://htmx.org/examples/update-other-content/)
1. [The multi-swap Extension](https://htmx.org/extensions/multi-swap/)
