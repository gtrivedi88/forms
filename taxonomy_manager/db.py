    <fieldset class="product-alias-group">
        <legend>Product Alias Information</legend>
        <label for="{{ form.alias_name.id }}">{{ form.alias_name.label }}</label>
        {{ form.alias_name(cols=40) }}
        
        <br><br>
        
        <label for="{{ form.alias_type.id }}">{{ form.alias_type.label }}</label>
        {{ form.alias_type(id="alias-type-dropdown", class="alias-type-dropdown") }}
        
        <br><br>

        <div class="form-group">
            <div class="checkbox-field">
                {{ form.alias_approved() }}
                <label for="{{ form.alias_approved.id }}" data-toggle="tooltip"
                    title="Leaving it blank for unapproved aliases.">{{ form.alias_approved.label }}</label>
            </div>
        
            <div class="checkbox-field">
                {{ form.previous_name() }}
                <label for="{{ form.previous_name.id }}">{{ form.previous_name.label }}</label>
            </div>
        
            <div class="checkbox-field">
                {{ form.tech_docs() }}
                <label for="{{ form.tech_docs.id }}">{{ form.tech_docs.label }}</label>
            </div>
        
            <div class="checkbox-field">
                {{ form.tech_docs_cli() }}
                <label for="{{ form.tech_docs_cli.id }}">{{ form.tech_docs_cli.label }}</label>
            </div>
        </div>
        
        <br><br>

        <label for="{{ form.alias_notes.id }}">{{ form.alias_notes.label }}</label>
        {{ form.alias_notes(cols=40) }}

        <br>
        <button type="button" class="add-alias-group" style="margin-top: 10px;">Add more aliases</button>
        <button type="button" class="remove-alias-group" style="display: none;">Delete</button>
    </fieldset>
