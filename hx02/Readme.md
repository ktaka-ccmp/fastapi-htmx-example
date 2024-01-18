# Load More from Database

A `Customer` list is stored in a SQLite database.
Upon a click on the load more button, an HTMX page reads more customers from the database.

<img src=../image/hx02-202401180439.gif width="600px">

# Updating two elements

Since the app placed the `Load more` button above the table, 
I could not use the way this ["Click to Load"](https://htmx.org/examples/click-to-load/) example shows.
For HTMX, updating multiple elements is doable.
However, it seems more challenging than updating a single element.
I followed the hx-swap-oob(Out of Band Responses) example.

In this example, not only the element "hx-target" points to but also the `bluebutton` itself has to be updated. 

The `bluebutton` element in the initial HTML template:
```
      <span id="bluebutton">
        <button class="px-3 py-1 bg-blue-600 text-white ml-4" hx-get="/hx02/list?skip={{ skip_next }}&limit={{ limit }}"
          hx-target="#table-body" hx-swap="beforeend" hx-trigger="click"> Load More
        </button>
      </span>
```

The fractional HTML template returned to the hx-get request:
```
{% for cs in customers %}
<tr>
  <td>{{ cs.id }}</td>
  <td>{{ cs.name }}</td>
  <td>{{ cs.email }}</td>
</tr>
{% endfor %}

<span id="bluebutton" hx-swap-oob="innerHTML:#bluebutton">
  <button class="px-3 py-1 bg-blue-600 text-white ml-4" hx-get="/hx02/list?skip={{ skip_next }}&limit={{ limit }}"
    hx-target="#table-body" hx-swap="beforeend" hx-trigger="click"> Load More
  </button>
</span>
```
> [!NOTE]
> * The `<span>` element with `hx-swap-oob` attribute must be placed after the `<tr>` element, otherwise it will mess up the layout. But I don't know why.
> * For the `hx-swap-oob` to be effective, `htmx.config.useTemplateFragments` needed to be set to true as:
>
> ```html
>  <meta name="htmx-config" content='{"useTemplateFragments":"true"}'>
> ```

Refs:
1. [Updating Other Content](https://htmx.org/examples/update-other-content/)
1. [The multi-swap Extension](https://htmx.org/extensions/multi-swap/)
